import api from "../../../api/axios";

export const login = (data) => {
    return api.post("/accounts/login/", data);
};

export const getProfile = () => {
    return api.get("/accounts/me/");
};