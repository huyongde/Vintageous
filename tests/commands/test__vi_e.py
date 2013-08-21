import unittest

from Vintageous.vi.constants import _MODE_INTERNAL_NORMAL
from Vintageous.vi.constants import MODE_NORMAL
from Vintageous.vi.constants import MODE_VISUAL
from Vintageous.vi.constants import MODE_VISUAL_LINE

from Vintageous.tests.commands import set_text
from Vintageous.tests.commands import add_selection
from Vintageous.tests.commands import get_sel
from Vintageous.tests.commands import first_sel
from Vintageous.tests.commands import BufferTest


# The heavy lifting is done by units.* functions, but we refine some cases in the actual motion
# command, so we need to test for that too here.
class Test_vi_e_InNormalMode(BufferTest):
    def testMoveToEndOfWord_OnLastLine(self):
        set_text(self.view, 'abc\nabc\nabc')
        r = self.R((2, 0), (2, 0))
        add_selection(self.view, a=r.a, b=r.b)

        self.view.run_command('_vi_e', {'mode': MODE_NORMAL, 'count': 1})

        expected = self.R((2, 2), (2, 2))
        self.assertEqual(expected, first_sel(self.view))

    def testMoveToEndOfWord_OnMiddleLine_WithTrailingWhitespace(self):
        set_text(self.view, 'abc\nabc   \nabc')
        r = self.R((1, 2), (1, 2))
        add_selection(self.view, a=r.a, b=r.b)

        self.view.run_command('_vi_e', {'mode': MODE_NORMAL, 'count': 1})

        expected = self.R((2, 2), (2, 2))
        self.assertEqual(expected, first_sel(self.view))

    def testMoveToEndOfWord_OnLastLine_WithTrailingWhitespace(self):
        set_text(self.view, 'abc\nabc\nabc   ')
        r = self.R((2, 0), (2, 0))
        add_selection(self.view, a=r.a, b=r.b)

        self.view.run_command('_vi_e', {'mode': MODE_NORMAL, 'count': 1})

        expected = self.R((2, 2), (2, 2))
        self.assertEqual(expected, first_sel(self.view))

        self.view.run_command('_vi_e', {'mode': MODE_NORMAL, 'count': 1})

        expected = self.R((2, 5), (2, 5))
        self.assertEqual(expected, first_sel(self.view))