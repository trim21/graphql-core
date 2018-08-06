"""graphql.validation.rules package"""

from typing import Type

from ...error import GraphQLError
from ...language.visitor import Visitor
from ..validation_context import ValidationContext

__all__ = ['ValidationRule', 'RuleType']


class ValidationRule(Visitor):

    def __init__(self, context: ValidationContext) -> None:
        self.context = context

    def report_error(self, error: GraphQLError):
        self.context.report_error(error)


RuleType = Type[ValidationRule]