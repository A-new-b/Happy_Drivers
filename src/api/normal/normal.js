import { axios } from "../request";
import { URL } from "../baseURL";

export function getData(data) {
  return axios({
    url: `${URL}data`,
    method: "post",
    data
  });
}

export function getSortMethod() {
  return axios({
    url: `${URL}sort/list`,
    method: "get"
  });
}

export function getSortResult(id, data) {
  return axios({
    url: `${URL}sort/${id}`,
    method: "post",
    data
  });
}

export function getSearchList() {
  return axios({
    url: `${URL}search/list`,
    method: "get"
  });
}

export function getSearchResult(id, data) {
  return axios({
    url: `${URL}search/${id}`,
    method: "post",
    data
  });
}

export function mapCreate(data) {
  return axios({
    url: `${URL}map`,
    method: "post",
    data
  });
}
