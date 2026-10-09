import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import RequestForm from "../components/RequestForm";

import {
    getCountries,
    getProvinces,
    getDistricts,
    getCapacities,
} from "../api/common";

import {
    createInstantRequest,
} from "../api/request";

export default function InstantRequest() {

    const navigate = useNavigate();

    const [loading, setLoading] = useState(false);

    const [countries, setCountries] = useState([]);

    const [provinces, setProvinces] = useState([]);

    const [districts, setDistricts] = useState([]);

    const [capacities, setCapacities] = useState([]);

    const [formData, setFormData] = useState({

        first_name: "",

        phone: "",

        request_type: "INSTANT",

        fulfillment_type: "SINGLE_DRIVER",

        service_type: "WATER",

        capacity_id: "",

        number_of_tankers: 1,

        budget_amount: "",

        country_id: "",

        province_id: "",

        district_id: "",

        delivery_address: "",

        latitude: "",

        longitude: "",

        notes: "",

    });

    useEffect(() => {

        loadCountries();

        loadCapacities();

    }, []);

    async function loadCountries() {

        const response = await getCountries();

        setCountries(response.data.data);

    }

    async function loadCapacities() {

        const response = await getCapacities();

        console.log("Capacity API:", response);

        console.log("Capacity Data:", response.data);

        setCapacities(response.data.data);

    }

    async function loadProvinces(countryId) {

        if (!countryId) {

            setProvinces([]);

            return;

        }

        const response = await getProvinces(countryId);

        setProvinces(response.data.data);

    }

    async function loadDistricts(provinceId) {

        if (!provinceId) {

            setDistricts([]);

            return;

        }

        const response = await getDistricts(provinceId);

        setDistricts(response.data.data);

    }

    function handleChange(e) {

        const { name, value } = e.target;

        setFormData((prev) => ({

            ...prev,

            [name]: value,

        }));

        if (name === "country_id") {

            loadProvinces(value);

            setDistricts([]);

        }

        if (name === "province_id") {

            loadDistricts(value);

        }

    }

    function useCurrentLocation() {

        if (!navigator.geolocation) {

            alert("Geolocation is not supported.");

            return;

        }

        navigator.geolocation.getCurrentPosition(

            (position) => {

                setFormData((prev) => ({

                    ...prev,

                    latitude: position.coords.latitude,

                    longitude: position.coords.longitude,

                }));

            },

            () => {

                alert("Unable to fetch location.");

            }

        );

    }

    async function handleSubmit(e) {

        e.preventDefault();

        try {

            setLoading(true);

            const response = await createInstantRequest(
                formData
            );

            navigate(
                "/request-success",
                {
                    state: response.data.data,
                }
            );

        }

        catch (error) {

            console.log(error);

            alert(
                error.response?.data?.message ??
                "Request failed."
            );

        }

        finally {

            setLoading(false);

        }

    }
    console.log("capacities state:", capacities);
    return (
        <div
            style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "flex-start", // use "center" for full vertical centering
                minHeight: "100vh",
                padding: "40px 20px",
                background: "#f5f5f5",
            }}
        >
            <div
                style={{
                    width: "100%",
                    maxWidth: "700px",
                    background: "#fff",
                    padding: "30px",
                    borderRadius: "10px",
                    boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
                }}
            >
                <RequestForm
                    formData={formData}
                    countries={countries}
                    provinces={provinces}
                    districts={districts}
                    capacities={capacities}
                    loading={loading}
                    onChange={handleChange}
                    onSubmit={handleSubmit}
                    onUseCurrentLocation={useCurrentLocation}
                />
            </div>
        </div>
    );

}