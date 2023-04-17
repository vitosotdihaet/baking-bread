import { ComponentStory, ComponentMeta } from '@storybook/react';
import { GoodTypeItem } from './GoodTypeItem';

export default {
    title: 'entities/Good/GoodTypeItem',
    component: GoodTypeItem,
} as ComponentMeta<typeof GoodTypeItem>;

const Template: ComponentStory<typeof GoodTypeItem> = (args) => <GoodTypeItem {...args} />;

export const Normal = Template.bind({});
Normal.args = {

};
