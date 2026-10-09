import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { getActiveJob } from "../api/jobs";
import { getInboxRequests } from "../api/requests";

export default function Dashboard() {

    const [activeJob, setActiveJob] = useState(null);

    const [requests, setRequests] = useState([]);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        loadDashboard();

    }, []);

    async function loadDashboard() {

        try {

            const [jobRes, requestRes] = await Promise.all([

                getActiveJob(),

                getInboxRequests(),

            ]);

            setActiveJob(
                jobRes.data.data
            );

            setRequests(
                requestRes.data.data || []
            );

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);

        }

    }

    if (loading) {

        return <h4>Loading...</h4>;

    }

    return (

        <div className="container-fluid">

            <h2 className="mb-4">

                Driver Dashboard

            </h2>

            <div className="card mb-4">

                <div className="card-header">

                    <strong>

                        🚚 Active Job

                    </strong>

                </div>

                <div className="card-body">

                    {
                        activeJob ?

                            <>

                                <h5>

                                    {activeJob.request_number}

                                </h5>

                                <p>

                                    Customer :
                                    {" "}
                                    {activeJob.customer}

                                </p>

                                <p>

                                    Address :
                                    {" "}
                                    {activeJob.address}

                                </p>

                                <p>

                                    Status :
                                    {" "}
                                    {activeJob.status}

                                </p>

                               <Link
                                    className="btn btn-primary"
                                    to="/driver/jobs"
                                >
                                    Continue
                                </Link>
                            </>

                            :

                            <p>

                                No active job.

                            </p>

                    }

                </div>

            </div>

            <div className="card">

                <div className="card-header">

                    <strong>

                        📥 Inbox

                    </strong>

                </div>

                <div className="card-body">

                    {
                        requests.length === 0 ?

                            <p>

                                No pending requests.

                            </p>

                            :

                            <table className="table table-bordered">

                                <thead>

                                    <tr>

                                        <th>

                                            Request

                                        </th>

                                        <th>

                                            Capacity

                                        </th>

                                        <th>

                                            Budget

                                        </th>

                                        <th>

                                            Status

                                        </th>

                                        <th>

                                        </th>

                                    </tr>

                                </thead>

                                <tbody>

                                    {
                                        requests.map(item => (

                                            <tr
                                                key={item.id}
                                            >

                                                <td>

                                                    {
                                                        item.request_number
                                                    }

                                                </td>

                                                <td>

                                                    {
                                                        item.capacity
                                                    }

                                                </td>

                                                <td>

                                                    {
                                                        item.budget_amount
                                                    }

                                                </td>

                                                <td>

                                                    {
                                                        item.response
                                                    }

                                                </td>

                                                <td>

                                                    <Link
                                                        className="btn btn-sm btn-primary"
                                                        to={`/driver/jobs/${item.id}`}
                                                    >

                                                        View

                                                    </Link>

                                                </td>

                                            </tr>

                                        ))
                                    }

                                </tbody>

                            </table>

                    }

                </div>

            </div>

        </div>

    );

}