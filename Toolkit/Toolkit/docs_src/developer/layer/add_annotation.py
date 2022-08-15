from openpecha.core.annotations import Citation, Span
from openpecha.core.layer import Layer, LayerEnum

layer = Layer(annotation_type=LayerEnum.citation)
ann = Citation(span=Span(start=10, end=20))

layer.set_annotation(ann)

assert ann.id in layer.annotations
