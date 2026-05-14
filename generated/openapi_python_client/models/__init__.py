"""Contains all the data models used in inputs/outputs"""

from .api_code_list import ApiCodeList
from .api_compare_indicators_across_countries import ApiCompareIndicatorsAcrossCountries
from .api_countries_across_all_goals import ApiCountriesAcrossAllGoals
from .api_countrywise_data import ApiCountrywiseData
from .api_dimension import ApiDimension
from .api_disaggregated_dimenions import ApiDisaggregatedDimenions
from .api_geo_area import ApiGeoArea
from .api_geo_tree import ApiGeoTree
from .api_goal import ApiGoal
from .api_goal_data import ApiGoalData
from .api_indicator import ApiIndicator
from .api_indicator_data import ApiIndicatorData
from .api_indicator_percentage import ApiIndicatorPercentage
from .api_multi_series_one_area import ApiMultiSeriesOneArea
from .api_observation import ApiObservation
from .api_observation_attributes import ApiObservationAttributes
from .api_observation_dimensions import ApiObservationDimensions
from .api_observation_page import ApiObservationPage
from .api_observation_pivot import ApiObservationPivot
from .api_observation_pivot_page import ApiObservationPivotPage
from .api_one_series_multi_area import ApiOneSeriesMultiArea
from .api_serie import ApiSerie
from .api_serie_data import ApiSerieData
from .api_series_data import ApiSeriesData
from .api_slice_data import ApiSliceData
from .api_slice_data_dimensions_item import ApiSliceDataDimensionsItem
from .api_target import ApiTarget
from .api_target_data import ApiTargetData
from .api_year_wise_data import ApiYearWiseData
from .concepts_master_data import ConceptsMasterData
from .entity_tag_header_value import EntityTagHeaderValue
from .file_result import FileResult
from .file_stream_result import FileStreamResult
from .goals_countrywise_data import GoalsCountrywiseData
from .sdg_goals import SDGGoals
from .sdmx_meta_data_response import SDMXMetaDataResponse
from .stream import Stream
from .string_segment import StringSegment
from .v1_sdg_compare_trends_get_area_by_series_disaggregation_dimensions_post_body import (
    V1SdgCompareTrendsGetAreaBySeriesDisaggregationDimensionsPostBody,
)
from .v1_sdg_compare_trends_get_data_multi_series_one_area_post_body import (
    V1SdgCompareTrendsGetDataMultiSeriesOneAreaPostBody,
)
from .v1_sdg_compare_trends_get_data_one_series_multi_area_post_body import (
    V1SdgCompareTrendsGetDataOneSeriesMultiAreaPostBody,
)
from .v1_sdg_compare_trends_get_series_disaggregation_dimensions_by_area_post_body import (
    V1SdgCompareTrendsGetSeriesDisaggregationDimensionsByAreaPostBody,
)
from .v1_sdg_data_availability_get_compareacrossgoal_data_post_body import (
    V1SdgDataAvailabilityGetCompareacrossgoalDataPostBody,
)
from .v1_sdg_data_availability_get_countries_across_goals_post_body import (
    V1SdgDataAvailabilityGetCountriesAcrossGoalsPostBody,
)
from .v1_sdg_data_availability_get_goals_disaggregated_data_post_body import (
    V1SdgDataAvailabilityGetGoalsDisaggregatedDataPostBody,
)
from .v1_sdg_data_availability_get_indicators_all_countries_post_body import (
    V1SdgDataAvailabilityGetIndicatorsAllCountriesPostBody,
)
from .v1_sdg_data_availability_get_series_aggregations_for_maps_post_body import (
    V1SdgDataAvailabilityGetSeriesAggregationsForMapsPostBody,
)
from .v1_sdg_data_availability_get_series_and_dis_aggregations_for_goals_post_body import (
    V1SdgDataAvailabilityGetSeriesAndDisAggregationsForGoalsPostBody,
)
from .v1_sdg_data_availability_get_worldby_goal_post_body import (
    V1SdgDataAvailabilityGetWorldbyGoalPostBody,
)
from .v1_sdg_feedback_add_feedback_post_body import V1SdgFeedbackAddFeedbackPostBody
from .v1_sdg_global_and_regional_get_multi_series_post_body import (
    V1SdgGlobalAndRegionalGetMultiSeriesPostBody,
)
from .v1_sdg_global_and_regional_get_single_series_post_body import (
    V1SdgGlobalAndRegionalGetSingleSeriesPostBody,
)
from .v1_sdg_goal_data_csv_post_body import V1SdgGoalDataCSVPostBody
from .v1_sdg_goal_data_excel_post_body import V1SdgGoalDataExcelPostBody
from .v1_sdg_series_data_count_post_body import V1SdgSeriesDataCountPostBody
from .v1_sdg_series_data_csv_post_body import V1SdgSeriesDataCSVPostBody
from .v1_sdg_series_data_excel_post_body import V1SdgSeriesDataExcelPostBody
from .v1_sdg_series_email_data_csv_post_body import V1SdgSeriesEmailDataCSVPostBody
from .v1_sdg_series_email_data_excel_post_body import V1SdgSeriesEmailDataExcelPostBody
from .v1_sdg_series_geo_area_code_post_body import V1SdgSeriesGeoAreaCodePostBody
from .v1_sdg_series_pivot_data_excel_post_body import V1SdgSeriesPivotDataExcelPostBody
from .v1_sdg_series_pivot_data_post_body import V1SdgSeriesPivotDataPostBody
from .v1_sdg_series_time_periods_post_body import V1SdgSeriesTimePeriodsPostBody

__all__ = (
    "ApiCodeList",
    "ApiCompareIndicatorsAcrossCountries",
    "ApiCountriesAcrossAllGoals",
    "ApiCountrywiseData",
    "ApiDimension",
    "ApiDisaggregatedDimenions",
    "ApiGeoArea",
    "ApiGeoTree",
    "ApiGoal",
    "ApiGoalData",
    "ApiIndicator",
    "ApiIndicatorData",
    "ApiIndicatorPercentage",
    "ApiMultiSeriesOneArea",
    "ApiObservation",
    "ApiObservationAttributes",
    "ApiObservationDimensions",
    "ApiObservationPage",
    "ApiObservationPivot",
    "ApiObservationPivotPage",
    "ApiOneSeriesMultiArea",
    "ApiSerie",
    "ApiSerieData",
    "ApiSeriesData",
    "ApiSliceData",
    "ApiSliceDataDimensionsItem",
    "ApiTarget",
    "ApiTargetData",
    "ApiYearWiseData",
    "ConceptsMasterData",
    "EntityTagHeaderValue",
    "FileResult",
    "FileStreamResult",
    "GoalsCountrywiseData",
    "SDGGoals",
    "SDMXMetaDataResponse",
    "Stream",
    "StringSegment",
    "V1SdgCompareTrendsGetAreaBySeriesDisaggregationDimensionsPostBody",
    "V1SdgCompareTrendsGetDataMultiSeriesOneAreaPostBody",
    "V1SdgCompareTrendsGetDataOneSeriesMultiAreaPostBody",
    "V1SdgCompareTrendsGetSeriesDisaggregationDimensionsByAreaPostBody",
    "V1SdgDataAvailabilityGetCompareacrossgoalDataPostBody",
    "V1SdgDataAvailabilityGetCountriesAcrossGoalsPostBody",
    "V1SdgDataAvailabilityGetGoalsDisaggregatedDataPostBody",
    "V1SdgDataAvailabilityGetIndicatorsAllCountriesPostBody",
    "V1SdgDataAvailabilityGetSeriesAggregationsForMapsPostBody",
    "V1SdgDataAvailabilityGetSeriesAndDisAggregationsForGoalsPostBody",
    "V1SdgDataAvailabilityGetWorldbyGoalPostBody",
    "V1SdgFeedbackAddFeedbackPostBody",
    "V1SdgGlobalAndRegionalGetMultiSeriesPostBody",
    "V1SdgGlobalAndRegionalGetSingleSeriesPostBody",
    "V1SdgGoalDataCSVPostBody",
    "V1SdgGoalDataExcelPostBody",
    "V1SdgSeriesDataCountPostBody",
    "V1SdgSeriesDataCSVPostBody",
    "V1SdgSeriesDataExcelPostBody",
    "V1SdgSeriesEmailDataCSVPostBody",
    "V1SdgSeriesEmailDataExcelPostBody",
    "V1SdgSeriesGeoAreaCodePostBody",
    "V1SdgSeriesPivotDataExcelPostBody",
    "V1SdgSeriesPivotDataPostBody",
    "V1SdgSeriesTimePeriodsPostBody",
)
