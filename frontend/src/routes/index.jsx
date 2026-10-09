import { createBrowserRouter } from "react-router-dom";

import PublicLayout from "../layouts/PublicLayout";
import DashboardLayout from "../layouts/DashboardLayout";

import Home from "../features/public/pages/Home";
import Login from "../features/accounts/pages/Login";
import NotFound from "../features/public/pages/NotFound";

import CreateRequest from "../features/customer/pages/CreateRequest";
import CustomerDashboard from "../features/customer/pages/Dashboard";



import DriverDashboard from "../features/driver/pages/Dashboard";
import Jobs from "../features/driver/pages/Jobs";
import JobDetail from "../features/driver/pages/JobDetail"
import History from "../features/driver/pages/History";
import JobHistoryDetail from "../features/driver/pages/JobHistoryDetail";


import ProviderDashboard from "../features/provider/pages/Dashboard";

import AdminDashboard from "../features/admin/pages/Dashboard";

import InstantRequest from "../features/customer/pages/InstantRequest";
import RequestSuccess from "../features/customer/pages/RequestSuccess";
import RequestDetail from "../features/customer/pages/RequestDetail";
import TrackRequest from "../features/customer/pages/TrackRequest";

const router = createBrowserRouter([
    {
        path: "/",
        element: <PublicLayout />,
        errorElement: <NotFound />,
        children: [
            {
                index: true,
                element: <Home />,
            },
            {
                path: "login",
                element: <Login />,
            },
            {
                path: "instant-request",
                element: <InstantRequest />,
            },
             {
            path: "/request-success",
                element: <RequestSuccess />,
            },

            {
                path: "/track-request",
                element: <TrackRequest />,
            },

            {
                path: "*",
                element: <NotFound />,
            },
        ],
    },

    {
        path: "/customer",
        element: <DashboardLayout />,
        children: [
            {
                index: true,
                element: <CustomerDashboard />,
            },
            {
                path: "request/:uuid",
                element: <RequestDetail />,
            },
            {
                path: "track/:uuid",
                element: <TrackRequest />,
            },
        ],
    },

    {
        path: "/driver",
        element: <DashboardLayout />,
        children: [
            {
                index: true,
                element: <DriverDashboard />,
            },
            {
                path: "jobs",
                element: <Jobs />,
            },
            {
                path: "jobs/history",
                element: <History />,
            },
            {
                path: "jobs/:id",
                element: <JobDetail />,
            },
            {
                path: "history/:id",
                element: <JobHistoryDetail />,
            },
        ],
    },

    {
        path: "/provider",
        element: <DashboardLayout />,
        children: [
            {
                index: true,
                element: <ProviderDashboard />,
            },
        ],
    },

    {
        path: "/admin",
        element: <DashboardLayout />,
        children: [
            {
                index: true,
                element: <AdminDashboard />,
            },
        ],
    },
]);

export default router;