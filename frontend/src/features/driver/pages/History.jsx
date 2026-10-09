import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { getJobHistory } from "../api/jobs";

export default function History() {

    const [jobs, setJobs] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {

        const loadHistory = async () => {

            try {

                const res = await getJobHistory();

                setJobs(res.data.data);

            } catch (err) {

                console.error(err);

            } finally {

                setLoading(false);

            }

        };

        loadHistory();

    }, []);

    if (loading) {
        return <h3>Loading...</h3>;
    }

    return (
        <div className="container">

            <h3>Job History</h3>

            <table className="table table-bordered">

                <thead>
                    <tr>
                        <th>Request</th>
                        <th>Customer</th>
                        <th>Tanker</th>
                        <th>Status</th>
                        <th>Completed</th>
                        <th></th>
                    </tr>
                </thead>

                <tbody>

                    {jobs.map((job) => (

                        <tr key={job.id}>

                            <td>{job.request_number}</td>

                            <td>{job.customer_name}</td>

                            <td>{job.plate_number}</td>

                            <td>{job.allocation_status}</td>

                            <td>{job.completed_at}</td>

                            <td>
                                <Link
                                    to={`/driver/history/${job.id}`}
                                    className="btn btn-sm btn-primary"
                                >
                                    View
                                </Link>
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>
    );
}