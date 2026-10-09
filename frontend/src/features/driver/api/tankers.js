import api from "../../../api/axios";

export function getTankers() {
    return api.get(
        "/driver/tankers/"
    );
}