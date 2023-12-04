import os

from epyk.core.Page import Report


def refresh(view_name):
    """
  Description:
  ------------
  This will transpile only the selected report.
  Transpilation will generate HTML content from the python code using Epyk framework

  Attributes:
  ----------
  :param view_name:
  """
    mod = __import__(view_name)
    page = Report()
    mod.get_page(page)
    print(page.outs.html_file(path=os.path.join('app', 'templates', 'views'), name=view_name))
