"""
Little example python-script that shows:
- how to apply a stylesheet to an XML file
- how a stylesheet can do more than just alter xml -- in this case, it performs a calculation

Notes...
- Note that the files are read as bytes, cuz otherwise the unicode-str will conflict
  with the encoding in the "XML declaration" (first line) of the xml files.
- If running under windows, and the `assert ( result_str == expected )` fails,
  comment out the line -- it could be that windows is defaulting to a different newline character(s).

Usage...
  Assumptions:
  - virtual-environment has been set up at sibling-level to xslt_exploration
  - lxml has been installed (see requirements.txt) into it
  Commands:
  $ cd /to/xslt_exploration
  $ source ../env/bin/activate
  $ python ./transform_code.py

  The 'print' statement at the end will print the result to the console.
"""

from lxml import etree

## laod source XML --------------------------------------------------
source_xml = b''
with open( './source_files/source.xml', 'rb' ) as f:
    source_xml = f.read()
assert type(source_xml) == bytes

## load stylesheet --------------------------------------------------
xslt_stylesheet = b''
with open( './source_files/stylesheet.xsl', 'rb' ) as f:
    xslt_stylesheet = f.read()
assert type(xslt_stylesheet) == bytes

## create XML tree objects ------------------------------------------
source_tree = etree.fromstring(source_xml)
xslt_tree = etree.fromstring(xslt_stylesheet)

## create transformer object ----------------------------------------
transform = etree.XSLT(xslt_tree)

## apply transformation ---------------------------------------------
result_tree = transform(source_tree)

## convert result tree-object to string -----------------------------
result_str = etree.tostring( result_tree, pretty_print=True).decode( 'utf-8' )
assert type(result_str) == str

## check output -----------------------------------------------------
expected = """<scores>
  <Person>
    <Name>Person 1</Name>
    <average>83.8</average>
  </Person>
  <Person>
    <Name>Person 2</Name>
    <average>87.0</average>
  </Person>
  <Person>
    <Name>Person 3</Name>
    <average>84.0</average>
  </Person>
</scores>
"""
assert ( result_str == expected )  # note that the closing </scores> is followed by a newline

## print output -----------------------------------------------------
print( result_str )
