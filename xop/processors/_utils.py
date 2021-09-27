from typing import List

from lxml import etree

from ..datatypes import BinaryContent, XmlInfoset, XopPackage


def replace_element_with_xop_include(element: etree._Element, cid: str) -> None:
    xop_include_el = etree.Element(
        "{http://www.w3.org/2004/08/xop/include}Include", href=f"cid:{cid}"
    )
    element.clear()
    element.append(xop_include_el)
