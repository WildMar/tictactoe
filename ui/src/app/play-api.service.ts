import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {catchError, map} from 'rxjs/operators';
import {Observable, of} from 'rxjs';
import {environment} from '../environments/environment';
import {BoardModel} from './board.model';

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

    startGame(): Observable<BoardModel> {
        return this.http
            .get<BoardModel>(`${environment.apiUrl}/game`)
            .pipe(map(data => new BoardModel().deserialize(data),
                catchError(this.handleError<BoardModel>('startGame'))));
    }

    //
    // makeMove(board?: PlayModel): Observable<PlayModel> {
    //
    //     return this.http
    //         .post(`${environment.apiUrl}/game`, board)
    //         .pipe(tap(_ => console.log("sent a thing"),
    //             catchError(this.handleError<PlayModel>("makeMove", []))))
    // }
}