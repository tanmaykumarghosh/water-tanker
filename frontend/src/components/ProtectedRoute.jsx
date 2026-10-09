import { Navigate } from "react-router-dom";

import useAuth from "../hooks/useAuth";

export default function ProtectedRoute({

    children,

    roles = [],

}) {

    const {

        loading,

        isAuthenticated,

        user,

    } = useAuth();

    if (loading) {

        return <h3>Loading...</h3>;

    }

    if (!isAuthenticated) {

        return <Navigate to="/login" replace />;

    }

    if (

        roles.length > 0 &&

        !roles.includes(user.role)

    ) {

        return <Navigate to="/" replace />;

    }

    return children;

}