import os
import sys

from epyk.core.Page import Report

template_path = os.path.join('views', 'reports')
sys.path.append(template_path)

if __name__ == '__main__':
    """
  This will transpile all the reports in the reports folder
  """
    for report in os.listdir(template_path):
        if report.endswith(".py"):
            view_name = report[:-3]
            mod = __import__(view_name)
            page = Report()
            mod.get_page(page)
            print(page.outs.html_file(path=os.path.join('views', 'templates', 'views'), name=view_name))
