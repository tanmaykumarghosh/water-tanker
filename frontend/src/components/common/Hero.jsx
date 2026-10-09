import { Link } from "react-router-dom";

export default function Hero() {
    return (
        <section
            style={{
                padding: "80px 20px",
                textAlign: "center",
            }}
        >
            <h1>Water Tanker Booking Platform</h1>

            <p>
                Book nearby water tankers within minutes.
            </p>

            <div
                style={{
                    marginTop: "30px",
                }}
            >
                <Link
                    to="/instant-request"
                    style={{
                        padding: "12px 25px",
                        marginRight: "20px",
                        border: "1px solid #333",
                    }}
                >
                    Instant Water Request
                </Link>

                <Link
                    to="/contract-request"
                    style={{
                        padding: "12px 25px",
                        border: "1px solid #333",
                    }}
                >
                    Contract Water Supply
                </Link>
            </div>
        </section>
    );
}