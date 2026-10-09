import { useState } from "react";
import { useNavigate } from "react-router-dom";

import useAuth from "../../../hooks/useAuth";

export default function Login() {

    const navigate = useNavigate();

    const { login } = useAuth();

    const [phone, setPhone] = useState("");
    const [password, setPassword] = useState("");

    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {

        e.preventDefault();

        setLoading(true);

        try {

            const user = await login(
                phone,
                password,
            );


            switch (user.role) {

                case "CUSTOMER":

                    navigate("/customer");

                    break;


                case "DRIVER":

                    navigate("/driver");

                    break;


                case "PROVIDER":

                    navigate("/provider");

                    break;


                default:

                    navigate("/");

            }


        } catch (error) {

            console.error(error);

            alert(
                error.response?.data?.message ||
                "Login failed."
            );

        } finally {

            setLoading(false);

        }
    };

    return (
        <div
            style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "flex-start",
                minHeight: "100vh",
                padding: "40px 20px",
                background: "#f5f5f5",
            }}
        >
            <div
                style={{
                    width: "100%",
                    maxWidth: "700px",
                    background: "#fff",
                    padding: "30px",
                    borderRadius: "10px",
                    boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
                }}
            >
                <h2 className="text-center mb-4">Login</h2>

                <form onSubmit={handleSubmit}>
                    <div className="mb-4">
                        <label
                            htmlFor="phone"
                            className="form-label"
                            style={{
                                display: "block",
                                marginBottom: "10px",
                                fontWeight: "500",
                            }}
                        >
                            Phone
                        </label>

                        <input
                            id="phone"
                            type="text"
                            className="form-control"
                            placeholder="Enter your phone number"
                            value={phone}
                            onChange={(e) => setPhone(e.target.value)}
                        />
                    </div>

                    <div className="mb-4">
                        <label
                            htmlFor="password"
                            className="form-label"
                            style={{
                                display: "block",
                                marginBottom: "10px",
                                fontWeight: "500",
                            }}
                        >
                            Password
                        </label>

                        <input
                            id="password"
                            type="password"
                            className="form-control"
                            placeholder="Enter your password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>

                    <button
                        type="submit"
                        className="btn btn-primary w-100"
                        disabled={loading}
                        style={{
                            padding: "10px",
                            fontWeight: "600",
                        }}
                    >
                        {loading ? "Logging in..." : "Login"}
                    </button>
                </form>
            </div>
        </div>
    );
}