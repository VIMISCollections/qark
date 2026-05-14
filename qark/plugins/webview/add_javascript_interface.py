import logging

from qark.issue import Issue, Severity
from qark.plugins.helpers import valid_method_invocation
from qark.scanner.plugin import CoroutinePlugin, ManifestPlugin

log = logging.getLogger(__name__)

ADD_JAVASCRIPT_INTERFACE_DESCRIPTION = (
    "This webview uses the addJavascriptInterface method in a pre-API 17 app, which exposes all public methods to "
    "Javascript running in the WebView. If this webview loads untrusted content or trusted content over plain-text "
    "HTTP, this represents a MAJOR issue! Reference: "
    "https://labs.mwrinfosecurity.com/blog/2013/09/24/webview-addjavascriptinterface-remote-code-execution/. "
    "To validate this vulnerability, load the following local file in this WebView: "
    "file://qark/poc/html/BAD_JS_INT.html"
)


class AddJavascriptInterface(CoroutinePlugin, ManifestPlugin):
    """This plugin checks if the `addJavaScriptInterface` method is called with a min_sdk of below 17."""
    def __init__(self):
        super(AddJavascriptInterface, self).__init__(category="webview",
                                                     name="Webview uses addJavascriptInterface pre-API 17",
                                                     description=ADD_JAVASCRIPT_INTERFACE_DESCRIPTION)
        self.severity = Severity.WARNING
        self.java_method_name = "addJavascriptInterface"

    def can_run_coroutine(self):
        return self.min_sdk <= 16

    def run_coroutine(self):
        '''
        The yield keyword is used to create generators. Special types of iterators that allow values to be produced one at a time, instead of all at once, and it remembers where it left off.
        '''
        while True:
            _, method_invocation = (yield)
            '''best I can guess here is that the method_invocation is from the AST. It checks if the current method in the AST is equal to "addJavascriptInterface" from line 26, with the expected nr. of parameters (2). This plugin also only runs for sdks <= 16. 
            '''
            if valid_method_invocation(method_invocation, method_name=self.java_method_name, num_arguments=2):
                self.issues.append(Issue(category=self.category, name=self.name, severity=self.severity,
                                         description=self.description, line_number=method_invocation.position,
                                         file_object=self.file_path))


plugin = AddJavascriptInterface()
