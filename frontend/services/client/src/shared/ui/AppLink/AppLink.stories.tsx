import { ComponentStory, ComponentMeta } from '@storybook/react';
import { AppLink } from './AppLink';

export default {
    title: 'shared/AppLink',
    component: AppLink,
    argTypes: {
        backgroundColor: { control: 'color' },
    },
} as ComponentMeta<typeof AppLink>;

const Template: ComponentStory<typeof AppLink> = (args) => <AppLink { ...args } />;

export const Normal = Template.bind({});
Normal.args = {

};
