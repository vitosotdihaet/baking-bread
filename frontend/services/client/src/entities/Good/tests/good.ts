import { Good, GoodType, GoodTypeWithGoods } from '../model/types/goods';
import cinnabonImage from './cinnabon.png';
import croissantsImage from './croissants.png';
import maccaronsImage from './maccarons.png';

export const mockedGood: Good = {
    available: true,
    description: 'Savory, hearty, meaty and messy! Just how we like it!',
    id: 7,
    image: maccaronsImage,
    lifetime: 2,
    name: 'Maccarons',
    previousPrice: 599,
    price: 3,
    quantity: 2,
    weight: 80,
};

export const mockedListGoods: Good[] = [
    {
        available: true,
        description: 'Savory, hearty, meaty and messy! Just how we like it!',
        id: 7,
        image: maccaronsImage,
        lifetime: 2,
        name: 'Maccarons',
        previousPrice: 599,
        price: 3,
        quantity: 2,
        weight: 80,
    },
    {
        available: false,
        description: 'Savory, hearty, meaty and messy! Just how we like it!',
        id: 7,
        image: croissantsImage,
        lifetime: 2,
        name: 'Croissants',
        previousPrice: 599,
        price: 3,
        quantity: 3,
        weight: 120,
    },
    {
        available: true,
        description: 'Savory, hearty, meaty and messy! Just how we like it!',
        id: 7,
        image: cinnabonImage,
        lifetime: 2,
        name: 'Cinnabons',
        previousPrice: 599,
        price: 1,
        quantity: 1,
        weight: 110,
    },
    {
        available: true,
        description: 'Savory, hearty, meaty and messy! Just how we like it!',
        id: 7,
        image: maccaronsImage,
        lifetime: 2,
        name: 'Maccarons',
        previousPrice: 599,
        price: 3,
        quantity: 2,
        weight: 80,
    },
    {
        available: false,
        description: 'Savory, hearty, meaty and messy! Just how we like it!',
        id: 7,
        image: croissantsImage,
        lifetime: 2,
        name: 'Croissants',
        previousPrice: 599,
        price: 3,
        quantity: 3,
        weight: 120,
    },
    {
        available: true,
        description: 'Savory, hearty, meaty and messy! Just how we like it!',
        id: 7,
        image: cinnabonImage,
        lifetime: 2,
        name: 'Cinnabons',
        previousPrice: 599,
        price: 1,
        quantity: 1,
        weight: 110,
    },
];

export const mockedGoodType: GoodTypeWithGoods = {
    id: 1,
    name: 'Savory pastries',
    description: 'For the savory lovers out there, our selection of hearty pies, quiches, and empanadas is sure to hit the spot!',
    goodsCount: 0,
    order: 0,
    goods: [...mockedListGoods],
};

export const mockedListGoodType: GoodType[] = [
    {
        id: 1,
        name: 'Savory pastries',
        description: 'For the savory lovers out there, our selection of hearty pies, quiches, and empanadas is sure to hit the spot!',
        goodsCount: 1,
        order: 0,
    },
    {
        id: 2,
        name: 'Sweet pastries',
        description: 'For the savory lovers out there, our selection of hearty pies, quiches, and empanadas is sure to hit the spot!',
        goodsCount: 1,
        order: 0,
    },
    {
        id: 3,
        name: 'Breads',
        description: 'For the savory lovers out there, our selection of hearty pies, quiches, and empanadas is sure to hit the spot!',
        goodsCount: 1,
        order: 0,
    },
];
