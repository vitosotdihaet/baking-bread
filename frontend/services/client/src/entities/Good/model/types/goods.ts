export interface GoodType {
    id: number;
    name: string;
    goodsCount: number;
    order: number;
    description: string;
}

export interface Good {
    id: number;
    available: boolean;
    description: string;
    image: string;
    lifetime: number;
    name: string;
    previousPrice: number;
    price: number;
    quantity: number;
    weight: number;
}

export interface GoodTypeWithGoods extends GoodType {
    goods: Good[];
}
