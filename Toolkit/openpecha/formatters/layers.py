"""
This module contains format variable for all the annotations
"""

from collections import namedtuple

__all__ = [
    "Layer",
    "Page",
    "Span",
    "Text",
    "Correction",
    "ErrorCandidate",
    "CrossVolSpan",
    "SubText",
    "Peydurma",
    "Chapter",
    "Tsawa",
    "Citation",
    "Sabche",
    "Yigchung",
    "BookTitle",
    "SubTitle",
    "BookNumber",
    "PotiTitle",
    "Author",
    "Archaic",
    "Span",
    "Footnote",
]


class AnnType:
    book_title = "BookTitle"
    sub_title = "SubTitle"
    book_number = "BookNumber"
    poti_title = "PotiTitle"
    author = "Author"
    chapter = "Chapter"

    topic = "Text"
    sub_topic = "SubText"

    pagination = "Pagination"
    citation = "Citation"
    correction = "Correction"
    error_candidate = "ErrorCandidate"
    peydurma = "Peydurma"
    pedurma_note = "PedurmaNote"
    sabche = "Sabche"
    tsawa = "Tsawa"
    yigchung = "Yigchung"
    archaic = "Archaic"
    durchen = "Durchen"
    footnote = "Footnote"


class _attr_names:
    # Layer
    ID = "id"  # Uique id for annotation of specific Pecha or Abstract work. type: str
    ANNOTATION_TYPE = "annotation_type"  # Name of annotation, type: str
    REVISION = "revision"  # Revision number. type: int
    ANNOTATION = "annotations"  # Annotations are stored in list . type: dict
    LOCAL_ID = "local_ids"

    # Spans
    SPAN = "span"
    VOL = "vol"
    START = "start"
    END = "end"

    # Page
    IMGNUM = "imgnum"
    PAGE_INDEX = "page_index"  # Page number based on Volume specified, type: int
    PAGE_REFERENCE = "reference"  # Any reference of page, eg: img_url. type: str

    # Text
    WORK_ID = "work_id"

    # Correction
    CORRECTION = "correction"  # Correct text suggestion. type: str
    CERTAINTY = "certainty"  # Certainty of the suggested correct text. type: int

    # Peydurma
    NOTE = "note"  # syls, word or phrase to be compared to other publication

    # Archaic word
    MODERN = "modern"

    # Tsawa, Citation
    ISVERSE = "isverse"  # Boolean flag to indicate a sache in verse format or not

    # Footnote
    FOOTNOTE_REF = "footnote_ref"


def Layer(id_, type_, rev=f"{1:05}"):
    return {
        _attr_names.ID: id_,
        _attr_names.ANNOTATION_TYPE: type_,
        _attr_names.REVISION: rev,
        _attr_names.ANNOTATION: {},
    }


def Span(start, end):
    return {_attr_names.START: start, _attr_names.END: end}


# ~~~ INDEX Layer ~~~~~
# Cross vol Span
CrossVolSpan = {"vol": None, "span": None}


def CrossVolSpan(vol, start, end):
    return {_attr_names.VOL: vol, _attr_names.START: start, _attr_names.END: end}


# Sub_text annotation
SubText = {"work": None, "span": []}  # index of the sub_text  # span of the sub_text

# Text annotation
Text = {
    "parts": [],
    "span": [],
    "work_id": "",
}  # list of SubText  # list of CrossVolSpan

# ~~~~~ ANNOTATIONS Layers ~~~~~~


def Page(span, imgnum=None, page_ref=None):
    return {
        _attr_names.IMGNUM: imgnum,
        _attr_names.PAGE_REFERENCE: page_ref,
        _attr_names.SPAN: span,
    }


def Correction(span, correction=None, certainty=None):
    return {
        _attr_names.CORRECTION: correction,
        # _attr_names.CERTAINTY: certainty,
        _attr_names.SPAN: span,
    }


def Archaic(span, modern=None, certainty=None):
    return {
        _attr_names.MODERN: modern,
        # _attr_names.CERTAINTY: certainty,
        _attr_names.SPAN: span,
    }


def ErrorCandidate(span):
    return {_attr_names.SPAN: span}


def Peydurma(span, note=None):
    return {_attr_names.NOTE: note, _attr_names.SPAN: span}


def BookTitle(span):
    return {_attr_names.SPAN: span}


def SubTitle(span):
    return {_attr_names.SPAN: span}


def BookNumber(span):
    return {_attr_names.SPAN: span}


def PotiTitle(span):
    return {_attr_names.SPAN: span}


def Author(span):
    return {_attr_names.SPAN: span}


def Chapter(span):
    return {_attr_names.SPAN: span}


def Tsawa(span, isverse=False):
    return {_attr_names.SPAN: span, _attr_names.ISVERSE: isverse}


def Citation(span, isverse=False):
    return {_attr_names.SPAN: span, _attr_names.ISVERSE: isverse}


def Sabche(span, isverse=False):
    return {_attr_names.SPAN: span}


def Yigchung(span):
    return {_attr_names.SPAN: span}


def Footnote(span, footnote_ref):
    return {_attr_names.SPAN: span, _attr_names.FOOTNOTE_REF: footnote_ref}
