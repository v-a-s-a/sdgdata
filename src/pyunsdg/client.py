import httpx
from typing import List, Optional
from pyunsdg.models import ApiTarget, ApiObservationPage, ApiGeoArea, ApiGoal, ConceptsMasterData, SDMXMetaDataResponse

# standard UNSD API base URL
BASE_URL = "https://unstats.un.org/sdgapi/v1"

class UNSDClient:
    def __init__(self):
        self.client = httpx.Client(base_url=BASE_URL, timeout=30.0)

    def get_target_list(self, include_children: bool = True) -> List[ApiTarget]:
        """
        Fetches all targets, optionally including their indicators and series.
        """
        response = self.client.get("/sdg/Target/List", params={"includechildren": include_children})
        response.raise_for_status()
        data = response.json()
        return [ApiTarget(**item) for item in data]
    
    def get_goal_list(self) -> List[ApiGoal]:
        """
        Fetches all SDG goals.
        """
        response = self.client.get("/sdg/Goal/List")
        response.raise_for_status()
        data = response.json()
        return [ApiGoal(**item) for item in data]
    
    def get_indicator_list(self, include_series: bool = True) -> List[ApiTarget]:
        """
        Fetches all indicators, optionally including their series.
        """
        response = self.client.get("/sdg/Indicator/List", params={"includechildren": include_series})
        response.raise_for_status()
        data = response.json()
        return [ApiTarget(**item) for item in data]
    
    def get_geo_area_list(self) -> List[ApiGeoArea]:
        """
        Fetches all geographic areas.
        """
        response = self.client.get("/sdg/GeoArea/List")
        response.raise_for_status()
        data = response.json()
        return [ApiGeoArea(**item) for item in data]

    def get_concept_list(self) -> List[ConceptsMasterData]:
        """
        Fetches all concepts. The API does not provide a structured model for concepts, so we return raw dicts.
        """
        response = self.client.get("sdg/SDMXMetadata/GetConceptsMasterList")
        response.raise_for_status()
        return [ConceptsMasterData(**item) for item in response.json()]
    
    def get_sdmx_series_list(self) -> List[SDMXMetaDataResponse]:
        """
        Fetches all SDMX series metadata. The API does not provide a structured model for SDMX metadata, so we return raw dicts.
        """
        response = self.client.get("sdg/SDMXMetadata/GetSeries")
        response.raise_for_status()
        return response.json()

    def get_series_data(
        self, 
        series_codes: List[str], 
        area_code: Optional[str] = None,
        start_period: Optional[str] = None,
        end_period: Optional[str] = None
    ) -> ApiObservationPage:
        """
        Pulls actual data observations for given series codes.
        """
        params = {
            "seriesCode": ",".join(series_codes),
        }
        if area_code:
            params["areaCode"] = area_code
        if start_period:
            params["timePeriodStart"] = start_period
        if end_period:
            params["timePeriodEnd"] = end_period

        # /sdg/Series/Data is often more direct than generic Observation for this
        response = self.client.get("/sdg/Series/Data", params=params)
        response.raise_for_status()
        
        # Validate response against the generated ApiObservationPage model
        return ApiObservationPage(**response.json())


    