import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {catchError, map, tap} from 'rxjs/operators';
import {Observable, of, pipe} from "rxjs";
import {environment} from "../environments/environment"
import {PlayModel} from "./play.model";

@Injectable()
export class PlayApiService {


    constructor(private http: HttpClient) {
    }

    private handleError<T>(operation = 'operation', result?: T) {
        return (error: any): Observable<T> => {
            console.error(error); // log to console instead
            return of(result as T);
        };
    }

    startGame(): Observable<PlayModel> {
        return this.http
            .get(`${environment.apiUrl}/game`)
            .pipe(tap(_ => console.log("got a thing"),
                catchError(this.handleError<PlayModel>("makeMove", []))))
    }

    makeMove(board?: PlayModel): Observable<PlayModel> {

        return this.http
            .post(`${environment.apiUrl}/game`, board)
            .pipe(tap(_ => console.log("sent a thing"),
                catchError(this.handleError<PlayModel>("makeMove", []))))
    }
}