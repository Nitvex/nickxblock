"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope


class NikitaXBlock(XBlock):
    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )
    has_score = True

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the NikitaXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/nickxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/nickxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/nickxblock.js"))
        frag.initialize_js('NikitaXBlock')
        return frag

    @XBlock.json_handler
    def check(self, data, suffix=''):
        self.runtime.publish(self, "grade",
                    { value: 1.0
                      max_value: 2.0 })

        return {"result": 1.0}    

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("NikitaXBlock",
             """<nickxblock/>
             """),
            ("Multiple NikitaXBlock",
             """<vertical_demo>
                <nickxblock/>
                <nickxblock/>
                <nickxblock/>
                </vertical_demo>
             """),
        ]
