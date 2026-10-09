import { useState } from "react";
import { trackRequest } from "../api/request";

export default function TrackRequest() {

    const [requestNumber, setRequestNumber] = useState("");
    const [phone, setPhone] = useState("");

    const [loading, setLoading] = useState(false);

    const [request, setRequest] = useState(null);

    const [error, setError] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await trackRequest({
                request_number: requestNumber,
                phone,
            });

            console.log(response.data);

            setRequest(response.data.data);
        } catch (error) {
            console.error(error);

            alert(
                error.response?.data?.message ||
                "Unable to track request."
            );
        }
    };

    return (

        <div className="container py-5">

            <div className="row justify-content-center">

                <div className="col-md-7">

                    <div className="card shadow">

                        <div className="card-header">

                            <h3>Track Your Request</h3>

                        </div>

                        <div className="card-body">

                            <form onSubmit={handleSubmit}>

                                <div className="mb-3">

                                    <label className="form-label">

                                        Request Number

                                    </label>

                                    <input
                                        className="form-control"
                                        value={requestNumber}
                                        onChange={(e) =>
                                            setRequestNumber(e.target.value)
                                        }
                                        required
                                    />

                                </div>

                                <div className="mb-3">

                                    <label className="form-label">

                                        Phone Number

                                    </label>

                                    <input
                                        className="form-control"
                                        value={phone}
                                        onChange={(e) =>
                                            setPhone(e.target.value)
                                        }
                                        required
                                    />

                                </div>

                                <button
                                    className="btn btn-primary w-100"
                                    disabled={loading}
                                >

                                    {loading
                                        ? "Tracking..."
                                        : "Track Request"}

                                </button>

                            </form>

                            {error && (

                                <div className="alert alert-danger mt-4">

                                    {error}

                                </div>

                            )}

                            {request && (

                                <div className="mt-4">

                                    <h4>

                                        Request Information

                                    </h4>

                                    <table className="table">

                                        <tbody>

                                            <tr>

                                                <th>

                                                    Request Number

                                                </th>

                                                <td>

                                                    {request.request_number}

                                                </td>

                                            </tr>

                                            <tr>

                                                <th>

                                                    Current Status

                                                </th>

                                                <td>

                                                    <span className="badge bg-success">

                                                        {request.status}

                                                    </span>

                                                </td>

                                            </tr>

                                        </tbody>

                                    </table>

                                    <h5 className="mt-4">

                                        Status History

                                    </h5>

                                    <ul className="list-group">

                                        {request.history.map(
                                            (item, index) => (

                                                <li
                                                    key={index}
                                                    className="list-group-item"
                                                >

                                                    <strong>

                                                        {item.status}

                                                    </strong>

                                                    <br />

                                                    {item.remarks}

                                                    <br />

                                                    <small>

                                                        {new Date(
                                                            item.created_at
                                                        ).toLocaleString()}

                                                    </small>

                                                </li>

                                            )
                                        )}

                                    </ul>

                                </div>

                            )}

                        </div>

                    </div>

                </div>

            </div>

        </div>
    );
}