import { Link } from "react-router-dom";

import useAuth from "../../hooks/useAuth";

export default function Header() {

    const { user } = useAuth();

    const dashboardLink = () => {

        switch (user?.role) {

            case "CUSTOMER":
                return "/customer";

            case "DRIVER":
                return "/driver";

            case "PROVIDER":
                return "/provider";

            case "ADMIN":
                return "/admin";

            default:
                return "/login";

        }

    };

    return (

        <header
            style={{
                padding: "15px 30px",
                borderBottom: "1px solid #ddd",
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
            }}
        >

            <h2>Water Tanker</h2>

            <nav
                style={{
                    display: "flex",
                    gap: "20px",
                    alignItems: "center",
                }}
            >

                <Link to="/">Home</Link>

                <a href="#about">About</a>

                <a href="#services">Services</a>

                <a href="#how-it-works">How It Works</a>

                <a href="#contact">Contact</a>

                <Link to={dashboardLink()}>

                    {user ? "Dashboard" : "Login"}

                </Link>

                <Link to="/customer/request">

                    Request Water

                </Link>

            </nav>

        </header>

    );

}