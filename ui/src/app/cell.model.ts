import {DeserializableModel} from './deserializable.model';

export class CellModel implements DeserializableModel {
    public value: string;

    deserialize(input: any): this {
        return Object.assign(this, input);
    }

    getValue() {
        return this.value;
    }
}
