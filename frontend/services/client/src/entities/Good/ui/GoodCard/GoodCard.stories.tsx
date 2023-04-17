import { ComponentStory, ComponentMeta } from '@storybook/react';
import { GoodCard } from './GoodCard';

export default {
    title: 'entities/Good/GoodCard',
    component: GoodCard,
} as ComponentMeta<typeof GoodCard>;

const Template: ComponentStory<typeof GoodCard> = (args) => <GoodCard {...args} />;

export const Normal = Template.bind({});
Normal.args = {};
