import { Navigate } from "react-router-dom";

import useAuth from "../hooks/useAuth";

import LoadingScreen from "../components/common/LoadingScreen";


export default function ProtectedRoute({
    children,
    roles = [],
}) {

    const {
        user,
        loading,
        isAuthenticated,
    } = useAuth();


    if (loading) {

        return <LoadingScreen />;

    }


    if (!isAuthenticated) {

        return (
            <Navigate
                to="/login"
                replace
            />
        );

    }


    if (
        roles.length &&
        !roles.includes(user.role)
    ) {

        return (
            <Navigate
                to="/"
                replace
            />
        );

    }


    return children;

}