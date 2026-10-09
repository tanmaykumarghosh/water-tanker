import api from "../../../api/axios";

export const getCountries = () =>
    api.get("/common/countries/");

export const getProvinces = (countryId) =>
    api.get(`/common/provinces/?country_id=${countryId}`);

export const getDistricts = (provinceId) =>
    api.get(`/common/districts/?province_id=${provinceId}`);

export const getCapacities = () =>
    api.get("/common/capacities/");