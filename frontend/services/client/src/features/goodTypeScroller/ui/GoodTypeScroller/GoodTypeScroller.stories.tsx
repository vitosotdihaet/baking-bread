import { ComponentStory, ComponentMeta } from '@storybook/react';
import { GoodTypeScroller } from './GoodTypeScroller';

export default {
    title: 'features/GoodTypeScroller',
    component: GoodTypeScroller,
} as ComponentMeta<typeof GoodTypeScroller>;

const Template: ComponentStory<typeof GoodTypeScroller> = (args) => <GoodTypeScroller {...args} />;

export const Normal = Template.bind({});
Normal.args = {

};
