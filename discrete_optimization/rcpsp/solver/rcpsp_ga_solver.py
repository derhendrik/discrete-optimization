from discrete_optimization.generic_tools.do_problem import (
    ObjectiveHandling,
    ParamsObjectiveFunction,
    build_aggreg_function_and_params_objective,
    build_evaluate_function_aggregated,
)
from discrete_optimization.generic_tools.do_solver import SolverDO
from discrete_optimization.generic_tools.ea.alternating_ga import AlternatingGa
from discrete_optimization.generic_tools.ea.ga import Ga
from discrete_optimization.generic_tools.ea.ga_tools import (
    ParametersAltGa,
    ParametersGa,
)
from discrete_optimization.generic_tools.result_storage.result_storage import (
    ResultStorage,
)
from discrete_optimization.rcpsp.rcpsp_model import (
    MultiModeRCPSPModel,
    PartialSolution,
    RCPSPModel,
    RCPSPModelCalendar,
    RCPSPSolution,
    SingleModeRCPSPModel,
)


class GA_RCPSP_Solver(SolverDO):
    def __init__(
        self,
        rcpsp_model: RCPSPModel,
        params_objective_function: ParamsObjectiveFunction = None,
        **kwargs
    ):
        self.rcpsp_model = rcpsp_model
        (
            self.aggreg_sol,
            self.aggreg_from_dict_values,
            self.params_objective_function,
        ) = build_aggreg_function_and_params_objective(
            self.rcpsp_model, params_objective_function=params_objective_function
        )

    def solve(self, parameters_ga: ParametersGa = ParametersGa.default_rcpsp(), **args):
        ga_solver = Ga(
            self.rcpsp_model,
            encoding=parameters_ga.encoding,
            objective_handling=parameters_ga.objective_handling,
            objectives=parameters_ga.objectives,
            objective_weights=parameters_ga.objective_weights,
            mutation=parameters_ga.mutation,
            max_evals=parameters_ga.max_evals,
        )
        return ga_solver.solve()


class GA_MRCPSP_Solver(SolverDO):
    def __init__(
        self,
        rcpsp_model: MultiModeRCPSPModel,
        params_objective_function: ParamsObjectiveFunction = None,
        **kwargs
    ):
        self.rcpsp_model = rcpsp_model
        (
            self.aggreg_sol,
            self.aggreg_from_dict_values,
            self.params_objective_function,
        ) = build_aggreg_function_and_params_objective(
            self.rcpsp_model, params_objective_function=params_objective_function
        )

    def solve(
        self, parameters_ga: ParametersAltGa = ParametersAltGa.default_mrcpsp(), **args
    ):
        ga_solver = AlternatingGa(
            self.rcpsp_model,
            encodings=parameters_ga.encodings,
            objective_handling=parameters_ga.objective_handling,
            objectives=parameters_ga.objectives,
            objective_weights=parameters_ga.objective_weights,
            mutations=parameters_ga.mutations,
            crossovers=parameters_ga.crossovers,
            max_evals=parameters_ga.max_evals,
            sub_evals=parameters_ga.sub_evals,
        )
        return ga_solver.solve()
