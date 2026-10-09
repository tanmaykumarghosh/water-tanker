import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { getMyRequests } from "../api/request";

export default function Dashboard() {

    const [requests, setRequests] = useState([]);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        loadRequests();

    }, []);

    const loadRequests = async () => {

        try {

            const response = await getMyRequests();

            setRequests(response.data.data);

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);

        }

    };

    if (loading) {

        return <h3>Loading...</h3>;

    }

    return (

        <div>

            <h2>My Requests</h2>

            <table className="table table-bordered">

                <thead>

                    <tr>

                        <th>Request No.</th>

                        <th>Service</th>

                        <th>Capacity</th>

                        <th>Status</th>

                        <th>Price</th>

                        <th>Action</th>

                    </tr>

                </thead>

                <tbody>

                    {requests.map((item) => (

                        <tr key={item.uuid}>

                            <td>{item.request_number}</td>

                            <td>{item.service}</td>

                            <td>{item.capacity}</td>

                            <td>{item.status}</td>

                            <td>{item.offered_price}</td>

                            <td>

                                <Link
                                    to={`/customer/request/${item.id}`}
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