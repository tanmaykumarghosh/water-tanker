import api from "../../../api/axios";

export function getInboxRequests() {
    return api.get(
        "/driver/requests/"
    );
}

export function getRequest(id) {
    return api.get(`/driver/requests/${id}/`);
}

export function acceptRequest(id, tankerId) {
    return api.post(
        `/driver/requests/${id}/accept/`,
        {
            tanker_id: tankerId,
        }
    );
}

export function rejectRequest(id) {
    return api.post(
        `/driver/requests/${id}/reject/`
    );
}