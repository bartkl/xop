from typing import List

from lxml import etree

from ..datatypes import BinaryContent, XmlInfoset, XopPackage


def _replace_element_with_xop_include(element: etree._Element, cid) -> None:
    xop_include_el = etree.Element(
        "{http://www.w3.org/2004/08/xop/include}Include", href=f"cid:{cid}"
    )
    element.clear()
    element.append(xop_include_el)


def optimize_content(
    original_xml_infoset: XmlInfoset,
    find_elements_to_optimize: etree.XPath,
    binary_contents: List[BinaryContent],
) -> XopPackage:
    elements_to_optimize = find_elements_to_optimize(original_xml_infoset)
    for element in elements_to_optimize:
        print(element.text)
        try:
            _, cid = element.text.split("cid:")
        except ValueError:
            raise ValueError(
                "Invalid data. Please identify the elements which have text of the form `cid:<CID>`."
            )

        _replace_element_with_xop_include(element, cid)

    xop_infoset = original_xml_infoset  # Processed.

    return XopPackage(xop_infoset=xop_infoset, optimized_content=binary_contents)
