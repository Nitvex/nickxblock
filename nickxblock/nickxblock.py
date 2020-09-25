"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope
from xblock.scorable import ScorableXBlockMixin, Score


class NikitaXBlock(ScorableXBlockMixin, XBlock):
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
    
    def has_submitted_answer(self):
        """
        Returns True if the user has made a submission.
        """
        return self.fields['count'].is_set_on(self)

    def max_score(self):  # pylint: disable=no-self-use
        """
        Return the problem's max score
        Required by the grading system in the LMS.
        """
        return 2
    
    def set_score(self, score):
        """
        Sets the score on this block.
        Takes a Score namedtuple containing a raw
        score and possible max (for this block, we expect that this will
        always be 1).
        """
        #assert score.raw_possible == self.max_score()
        #score.raw_earned = 1/2
        self.count = 1 #score.raw_earned

    def get_score(self):
        """
        Return the problem's current score as raw values.
        """        
        return Score(1, self.max_score())

    def calculate_score(self):
        """
        Returns a newly-calculated raw score on the problem for the learner
        based on the learner's current state.
        """
        return Score(1, self.max_score())

    @XBlock.json_handler
    def check(self, data, suffix=''):
        # self.runtime.publish(self, "grade",
        #             { value: 1.0,
        #               max_value: 2.0 })
        self._publish_grade(Score(1.0, 2.0))
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
