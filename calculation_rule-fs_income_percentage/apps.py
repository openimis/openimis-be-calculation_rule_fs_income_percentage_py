import importlib
import inspect
from django.apps import AppConfig
from calculation.apps import CALCULATION_RULES

from core.abs_calculation_rule import AbsCalculationRule


MODULE_NAME = "calculation_rule-fs_income_percentage"
DEFAULT_CFG = {}


class CalculationRuleFSIncomePercentageConfig(AppConfig):
    name = MODULE_NAME

    def ready(self):
        from core.models import ModuleConfiguration
        cfg = ModuleConfiguration.get_or_default(MODULE_NAME, DEFAULT_CFG)
        read_all_calculation_rules()
