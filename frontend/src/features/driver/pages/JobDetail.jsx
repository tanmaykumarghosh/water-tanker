import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";


import {
    getRequest,
    acceptRequest,
    rejectRequest,
} from "../api/requests";

import { getTankers } from "../api/tankers";

export default function JobDetail() {

    const { id } = useParams();

    const navigate = useNavigate();

    const [job, setJob] = useState(null);

    const [tankers, setTankers] = useState([]);

    const [tankerId, setTankerId] = useState("");

    useEffect(() => {

        loadData();

    }, []);

    async function loadData() {

        try {

            const [jobRes, tankerRes] = await Promise.all([
                getRequest(id),
                getTankers(),
            ]);

            setJob(
                jobRes.data.data
            );

            setTankers(
                tankerRes.data.data
            );

        } catch (error) {

            console.error(error);

        }

    }

    

    async function handleAccept() {

        if (!tankerId) {

            alert("Please select a tanker.");

            return;

        }

        try {

            await acceptRequest(
                id,
                tankerId,
            );

            alert(
                "Accepted successfully."
            );

            navigate("/driver");

        } catch (error) {

            alert(
                error.response?.data?.message ||
                "Unable to accept."
            );

        }

    }

    async function handleReject() {

        if (!window.confirm("Reject this request?"))
            return;

        try {

            await rejectRequest(id);

            alert(
                "Request rejected."
            );

            navigate("/driver");

        } catch (error) {

            alert(
                error.response?.data?.message ||
                "Unable to reject."
            );

        }

    }

    if (!job)
        return <h4>Loading...</h4>;

    return (

        <div className="container">

            <h2>

                {job.request_number}

            </h2>

            <hr/>

            <p>

                <strong>Customer:</strong>

                {" "}

                {job.customer_name}

            </p>

            <p>

                <strong>Phone:</strong>

                {" "}

                {job.phone}

            </p>

            <p>

                <strong>Address:</strong>

                {" "}

                {job.delivery_address}

            </p>

            <p>

                <strong>Capacity:</strong>

                {" "}

                {job.capacity}

            </p>

            <p>

                <strong>Budget:</strong>

                {" "}

                {job.budget_amount}

            </p>

            <p>

                <strong>Notes:</strong>

                {" "}

                {job.notes}

            </p>

            <div className="mb-3">

                <label>

                    Select Tanker

                </label>

                <select
                    className="form-select"
                    value={tankerId}
                    onChange={(e)=>
                        setTankerId(
                            e.target.value
                        )
                    }
                >

                    <option value="">

                        Select

                    </option>

                    {
                        tankers.map(t => (

                            <option
                                key={t.id}
                                value={t.id}
                            >

                                {t.plate_number}
                                {" - "}
                                {t.capacity}

                            </option>

                        ))
                    }

                </select>

            </div>

            <button
                className="btn btn-success me-2"
                onClick={handleAccept}
            >

                Accept

            </button>

            <button
                className="btn btn-danger"
                onClick={handleReject}
            >

                Reject

            </button>

        </div>

    );

}