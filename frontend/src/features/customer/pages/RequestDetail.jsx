import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import { getRequest } from "../api/request";

export default function RequestDetail() {

    const { uuid } = useParams();

    const [request, setRequest] = useState(null);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        loadRequest();

    }, []);

    const loadRequest = async () => {

        try {

            const response = await getRequest(uuid);

            setRequest(response.data.data);

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);

        }

    };

    if (loading) {

        return <h3>Loading...</h3>;

    }

    if (!request) {

        return <h3>Request not found.</h3>;

    }

    return (

        <div>

            <h2>Request Details</h2>

            <table className="table table-bordered">

                <tbody>

                    <tr>
                        <th>Request Number</th>
                        <td>{request.request_number}</td>
                    </tr>

                    <tr>
                        <th>Service</th>
                        <td>{request.service}</td>
                    </tr>

                    <tr>
                        <th>Capacity</th>
                        <td>{request.capacity}</td>
                    </tr>

                    <tr>
                        <th>Status</th>
                        <td>{request.status}</td>
                    </tr>

                    <tr>
                        <th>Offered Price</th>
                        <td>{request.offered_price}</td>
                    </tr>

                    <tr>
                        <th>Province</th>
                        <td>{request.province}</td>
                    </tr>

                    <tr>
                        <th>District</th>
                        <td>{request.district}</td>
                    </tr>

                    <tr>
                        <th>Address</th>
                        <td>{request.address}</td>
                    </tr>

                    <tr>
                        <th>Notes</th>
                        <td>{request.notes}</td>
                    </tr>

                    <tr>
                        <th>Created</th>
                        <td>{request.created_at}</td>
                    </tr>

                </tbody>

            </table>

        </div>

    );

}