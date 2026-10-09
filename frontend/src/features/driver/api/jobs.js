import api from "../../../api/axios";

export function getActiveJob() {
    return api.get(
        "/driver/jobs/active/"
    );
}

export function updateJobStatus(
    id,
    status,
    latitude,
    longitude,
    accuracy = null,
    speed = null,
    heading = null,
) {

    console.log(status);
    return api.post(
        `/driver/jobs/${id}/status/`,
        {
            status,
            latitude,
            longitude,
            accuracy,
            speed,
            heading,
        }
    );

}

export function getJobHistory() {
    return api.get("/driver/jobs/history/");
}

export function getHistoryDetail(id) {

    return api.get(
        `/driver/jobs/history/${id}/`
    );

}