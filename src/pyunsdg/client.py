import httpx
from typing import List, Optional
from pyunsdg.models import ApiTarget, ApiObservationPage, ApiGeoArea

# standard UNSD API base URL
BASE_URL = "https://unstats.un.org/sdgapi/v1"

class UNSDClient:
    def __init__(self):
        self.client = httpx.Client(base_url=BASE_URL, timeout=30.0)

    def get_all_targets(self, include_children: bool = True) -> List[ApiTarget]:
        """
        Fetches all targets, optionally including their indicators and series.
        """
        response = self.client.get("/sdg/Target/List", params={"includechildren": include_children})
        response.raise_for_status()
        data = response.json()
        return [ApiTarget(**item) for item in data]

    def get_target_metadata(self, target_code: str) -> List[ApiTarget]:
        """
        Fetches metadata for a specific target to find its indicators and series.
        Note: The API returns a list of all targets, so we filter client-side.
        """
        all_targets = self.get_all_targets(include_children=True)
        
        # Filter for the specific target code
        return [t for t in all_targets if t.code == target_code]

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

    def get_geo_areas(self) -> List[ApiGeoArea]:
        """
        Fetches all geographic areas.
        """
        response = self.client.get("/sdg/GeoArea/List")
        response.raise_for_status()
        data = response.json()
        return [ApiGeoArea(**item) for item in data]
