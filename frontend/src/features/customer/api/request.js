import api from "../../../api/axios";

export const createRequest = (data) => {
    return api.post(
        "/customer/service-requests/",
        data
    );
};
export function createInstantRequest(data) {
    return api.post(
        "/customer/public/instant-request/",
        data
    );
}
export const trackRequest = (data) => {
    return api.post(
        "/customer/public/track-request/",
        data
    );
};

export const getMyRequests = () => {
     return api.get("/customer/requests/");
};

export const getRequest = (uuid) => {
    return api.get(`/customer/requests/${uuid}/`);
};