import api from "../../../api/axios";

export function updateTracking(id, data) {
    return api.post(
        `/driver/jobs/${id}/tracking/`,
        data,
    );
}