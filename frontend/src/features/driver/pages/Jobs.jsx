import { useEffect, useState } from "react";
import { updateTracking } from "../api/tracking";
import {
    getActiveJob,
    updateJobStatus,
} from "../api/jobs";

export default function Jobs() {

    const [job, setJob] = useState(null);

    const [loading, setLoading] = useState(true);

    const loadJob = async () => {

        try {

            const res = await getActiveJob();
            console.log(res.data);

            setJob(res.data.data);

        } catch (err) {

            console.error(err);

        } finally {

            setLoading(false);

        }

    };

    useEffect(() => {
        loadJob();
    }, []);

    useEffect(() => {

        if (!job) return;

        const interval = setInterval(() => {
            sendLocation();
        }, 10000);

        return () => clearInterval(interval);

    }, [job?.id]);
    async function sendLocation() {

        if (!job?.id) {
            return;
        }

        if (!navigator.geolocation) {
            console.log("Geolocation not supported.");
            return;
        }

        console.log(job);

        navigator.geolocation.getCurrentPosition(
            async (position) => {

                try {

                    await updateTracking(
                        job.id,
                        {
                            latitude: position.coords.latitude,
                            longitude: position.coords.longitude,
                            accuracy: position.coords.accuracy != null
                                ? Number(position.coords.accuracy.toFixed(2))
                                : null,
                            speed: position.coords.speed,
                            heading: position.coords.heading,
                        }
                    );

                } catch (error) {

                    console.error(error);

                }

            }
        );
    }

    const handleStatus = async (status) => {

        if (!navigator.geolocation) {

            alert("Geolocation is not supported.");

            return;

        }

        navigator.geolocation.getCurrentPosition(

            async (position) => {

                try {

                    await updateJobStatus(

                        job.id,

                        status,

                        position.coords.latitude,

                        position.coords.longitude,

                       position.coords.accuracy != null
                            ? Number(position.coords.accuracy.toFixed(2))
                            : null,

                        position.coords.speed,

                        position.coords.heading,

                    );

                    await loadJob();

                }

                catch (err) {

                    alert(

                        err.response?.data?.message ||

                        "Unable to update."

                    );

                }

            },

            (error) => {

                console.error(error);

                alert("Unable to fetch current location.");

            },

            {

                enableHighAccuracy: true,

                timeout: 10000,

                maximumAge: 0,

            }

        );

    };

    if (loading) {

        return <h3>Loading...</h3>;

    }

    if (!job) {

        return (
            <div className="container">

                <h3>No Active Job</h3>

            </div>
        );

    }

    return (

        <div className="container">

            <div className="card">

                <div className="card-header">

                    <h3>

                        Active Job

                    </h3>

                </div>

                <div className="card-body">

                    <table className="table">

                        <tbody>

                            <tr>

                                <th>

                                    Request

                                </th>

                                <td>

                                    {job.request_number}

                                </td>

                            </tr>

                            <tr>

                                <th>

                                    Customer

                                </th>

                                <td>

                                    {job.customer_name}

                                </td>

                            </tr>

                            <tr>

                                <th>

                                    Phone

                                </th>

                                <td>

                                    {job.customer_phone}

                                </td>

                            </tr>

                            <tr>

                                <th>

                                    Address

                                </th>

                                <td>

                                    {job.delivery_address}

                                </td>

                            </tr>

                            <tr>

                                <th>

                                    Tanker

                                </th>

                                <td>

                                    {job.plate_number}

                                </td>

                            </tr>

                            <tr>

                                <th>

                                    Capacity

                                </th>

                                <td>

                                    {job.tanker_capacity}

                                </td>

                            </tr>

                            <tr>

                                <th>

                                    Status

                                </th>

                                <td>

                                    {job.allocation_status}

                                </td>

                            </tr>

                            <tr>

                                <th>

                                    Notes

                                </th>

                                <td>

                                    {job.notes}

                                </td>

                            </tr>

                        </tbody>

                    </table>

                    {job.allocation_status === "ACCEPTED" && (

                        <button
                            className="btn btn-primary"
                            onClick={() =>
                                handleStatus(
                                    "ARRIVED"
                                )
                            }
                        >

                            Arrived

                        </button>

                    )}

                    {job.allocation_status === "ARRIVED" && (

                        <button
                            className="btn btn-warning"
                            onClick={() =>
                                handleStatus(
                                    "ON_THE_WAY"
                                )
                            }
                        >

                            Depart

                        </button>

                    )}

                    {job.allocation_status === "ON_THE_WAY" && (

                        <button
                            className="btn btn-info"
                            onClick={() =>
                                handleStatus(
                                    "DELIVERY_STARTED"
                                )
                            }
                        >

                            Start Delivery

                        </button>

                    )}

                    {job.allocation_status === "DELIVERY_STARTED" && (

                        <button
                            className="btn btn-success"
                            onClick={() =>
                                handleStatus(
                                    "DELIVERED"
                                )
                            }
                        >

                            Complete Job

                        </button>

                    )}

                    {job.allocation_status === "DELIVERED" && (

                        <div
                            className="alert alert-success mt-3"
                        >

                            Job Completed

                        </div>

                    )}

                </div>

            </div>

        </div>

    );

}