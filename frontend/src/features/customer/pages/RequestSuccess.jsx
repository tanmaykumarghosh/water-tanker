import { useLocation, Link } from "react-router-dom";

export default function RequestSuccess() {

    const { state } = useLocation();

    return (
        <div>
            <h2>Request Submitted Successfully</h2>

            <p>
                Request Number:
                <strong> {state?.request_number}</strong>
            </p>

            <p>
                Status:
                <strong> {state?.status}</strong>
            </p>

            <Link to="/track-request">
                Track Request
            </Link>
        </div>
    );
}