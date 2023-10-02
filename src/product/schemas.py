from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class LoadTestLocust:
    timestamp: int
    user_count: int
    type_request: str
    name_request: str
    requests_s: float
    failures_s: float
    perc_50: int
    perc_66: int
    perc_75: int
    perc_80: int
    perc_90: int
    perc_95: int
    perc_98: int
    perc_99: int
    perc_999: int
    perc_9999: int
    perc_100: int
    total_request_count: int
    total_failure_count: int
    total_median_response_time: int
    total_average_response_time: float
    total_min_response_time: float
    total_max_response_time: float
    total_average_content_size: float

    class Config:
        orm_mode = True


class LoadTestLocustSummary:
    type_request: str
    name_request: str
    request_count: int
    failure_count: int
    median_response_time: int
    average_response_time: float
    min_response_time: float
    max_response_time: float
    average_content_size: float
    requests_s: float
    failures_s: float
    perc_50: int
    perc_66: int
    perc_75: int
    perc_80: int
    perc_90: int
    perc_95: int
    perc_98: int
    perc_99: int
    perc_999: int
    perc_9999: int
    perc_100: int

    class Config:
        orm_mode = True


class LoadTestYandexTank:
    time: int
    tag: str
    interval_real: int
    connect_time: int
    send_time: int
    latency: int
    receive_time: int
    interval_event: int
    size_out: int
    size_in: int
    net_code: int
    proto_code: int
