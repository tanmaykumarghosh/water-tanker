import { Navigate } from "react-router-dom";

import useAuth from "../hooks/useAuth";

export default function GuestRoute({

    children,

}) {

    const {

        loading,

        user,

    } = useAuth();

    if (loading) {

        return <h3>Loading...</h3>;

    }

    if (user) {

        switch (user.role) {

            case "CUSTOMER":

                return <Navigate to="/customer/dashboard" />;

            case "DRIVER":

                return <Navigate to="/driver/dashboard" />;

            case "PROVIDER":

                return <Navigate to="/provider/dashboard" />;

            default:

                break;

        }

    }

    return children;

}