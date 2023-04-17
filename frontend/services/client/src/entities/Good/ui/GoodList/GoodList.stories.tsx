import { ComponentStory, ComponentMeta } from '@storybook/react';
import { GoodList } from './GoodList';

export default {
    title: 'entities/Good/GoodList',
    component: GoodList,
} as ComponentMeta<typeof GoodList>;

const Template: ComponentStory<typeof GoodList> = (args) => <GoodList {...args} />;

export const Normal = Template.bind({});
Normal.args = {

};
