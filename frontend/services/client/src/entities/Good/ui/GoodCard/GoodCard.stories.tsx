import { ComponentStory, ComponentMeta } from '@storybook/react';
import { mockedGood } from '../../tests/good';
import { GoodCard } from './GoodCard';

export default {
    title: 'entities/Good/GoodCard',
    component: GoodCard,
} as ComponentMeta<typeof GoodCard>;

const Template: ComponentStory<typeof GoodCard> = (args) => <GoodCard {...args} />;

export const ManyPieces = Template.bind({});
ManyPieces.args = {
    good: mockedGood,
};

export const OnlyOnePiece = Template.bind({});
OnlyOnePiece.args = {
    good: {
        ...mockedGood,
        quantity: 1,
    },
};

export const Unavailable = Template.bind({});
Unavailable.args = {
    good: {
        ...mockedGood,
        available: false,
    },
};
