import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import { getHistoryDetail } from "../api/jobs";

export default function JobHistoryDetail() {

    const { id } = useParams();

    const [job, setJob] = useState(null);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        load();

    }, [id]);

    const load = async () => {

        try {

            const res = await getHistoryDetail(id);

            setJob(res.data.data);

        } catch (err) {

            console.error(err);

        } finally {

            setLoading(false);

        }

    };

    if (loading) {

        return <h4>Loading...</h4>;

    }

    if (!job) {

        return <h4>Job not found.</h4>;

    }

    return (

        <div className="container">

            <h2>{job.request_number}</h2>

            <hr />

            <table className="table table-bordered">

                <tbody>

                    <tr>
                        <th>Customer</th>
                        <td>{job.customer_name}</td>
                    </tr>

                    <tr>
                        <th>Phone</th>
                        <td>{job.customer_phone}</td>
                    </tr>

                    <tr>
                        <th>Address</th>
                        <td>{job.delivery_address}</td>
                    </tr>

                    <tr>
                        <th>Tanker</th>
                        <td>{job.plate_number}</td>
                    </tr>

                    <tr>
                        <th>Capacity</th>
                        <td>{job.tanker_capacity}</td>
                    </tr>

                    <tr>
                        <th>Budget</th>
                        <td>{job.budget_amount}</td>
                    </tr>

                    <tr>
                        <th>Status</th>
                        <td>{job.allocation_status}</td>
                    </tr>

                    <tr>
                        <th>Accepted At</th>
                        <td>{job.accepted_at}</td>
                    </tr>

                    <tr>
                        <th>Arrived At</th>
                        <td>{job.arrived_at}</td>
                    </tr>

                    <tr>
                        <th>Departed At</th>
                        <td>{job.departed_at}</td>
                    </tr>

                    <tr>
                        <th>Delivery Started</th>
                        <td>{job.delivery_started_at}</td>
                    </tr>

                    <tr>
                        <th>Completed At</th>
                        <td>{job.completed_at}</td>
                    </tr>

                    <tr>
                        <th>Notes</th>
                        <td>{job.notes}</td>
                    </tr>

                </tbody>

            </table>

        </div>

    );

}